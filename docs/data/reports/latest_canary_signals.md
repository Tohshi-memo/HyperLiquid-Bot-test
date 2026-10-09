# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T12:52:31.801354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1259` n `13`; crypto_alt avg `-0.2551` n `235`; crypto_major avg `-0.2908` n `8`; equity avg `-0.0921` n `150`; fx avg `-0.0084` n `6`; index avg `-0.0273` n `26`; metal avg `-0.0721` n `20`; unknown avg `1.9334` n `1078`
- 1h: commodity avg `0.1616` n `13`; crypto_alt avg `-0.6925` n `235`; crypto_major avg `-0.5491` n `8`; equity avg `-0.2403` n `150`; fx avg `-0.0327` n `6`; index avg `-0.055` n `26`; metal avg `-0.1058` n `20`; unknown avg `0.6374` n `1070`
- 4h: commodity avg `0.2624` n `13`; crypto_alt avg `-0.8222` n `235`; crypto_major avg `-0.2875` n `8`; equity avg `-0.2587` n `150`; fx avg `-0.0822` n `6`; index avg `-0.0841` n `26`; metal avg `-0.076` n `20`; unknown avg `1.7294` n `1070`
- 24h: commodity avg `-0.3388` n `13`; crypto_alt avg `-0.8493` n `235`; crypto_major avg `-0.8591` n `8`; equity avg `-0.2231` n `150`; fx avg `0.0048` n `6`; index avg `0.028` n `26`; metal avg `0.5208` n `20`; unknown avg `7.2771` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
