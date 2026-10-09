# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T10:37:33.697826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `13`; crypto_alt avg `-0.5131` n `235`; crypto_major avg `-0.2441` n `8`; equity avg `-0.0774` n `150`; fx avg `-0.002` n `6`; index avg `-0.0123` n `26`; metal avg `-0.021` n `20`; unknown avg `0.6172` n `1078`
- 1h: commodity avg `-0.015` n `13`; crypto_alt avg `-0.5074` n `235`; crypto_major avg `-0.3385` n `8`; equity avg `-0.0923` n `150`; fx avg `-0.0112` n `6`; index avg `-0.0265` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.4329` n `1076`
- 4h: commodity avg `-0.1273` n `13`; crypto_alt avg `-0.6683` n `235`; crypto_major avg `-0.3376` n `8`; equity avg `-0.0367` n `150`; fx avg `-0.022` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0217` n `20`; unknown avg `1.0405` n `1006`
- 24h: commodity avg `-0.5774` n `13`; crypto_alt avg `-1.837` n `235`; crypto_major avg `-1.9574` n `8`; equity avg `-0.1391` n `150`; fx avg `0.0558` n `6`; index avg `0.1197` n `26`; metal avg `0.5648` n `20`; unknown avg `7.5839` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
