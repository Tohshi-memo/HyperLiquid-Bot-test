# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T06:37:26.039554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.0125` n `235`; crypto_major avg `0.0314` n `8`; equity avg `-0.0142` n `143`; fx avg `0.0009` n `6`; index avg `0.0014` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.0748` n `1079`
- 1h: commodity avg `0.0015` n `13`; crypto_alt avg `-0.1113` n `235`; crypto_major avg `0.067` n `8`; equity avg `-0.0122` n `143`; fx avg `-0.0024` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.2648` n `1049`
- 4h: commodity avg `-0.0416` n `13`; crypto_alt avg `0.5243` n `235`; crypto_major avg `0.2665` n `8`; equity avg `0.0489` n `143`; fx avg `-0.0244` n `6`; index avg `0.0013` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.2827` n `1043`
- 24h: commodity avg `0.2045` n `13`; crypto_alt avg `1.8947` n `235`; crypto_major avg `0.9111` n `8`; equity avg `0.2734` n `143`; fx avg `-0.0354` n `6`; index avg `0.0205` n `26`; metal avg `0.0033` n `20`; unknown avg `0.3124` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
