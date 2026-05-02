# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T05:15:20.785394+00:00`
- Correlation status: `ready`
- Asset price records: `44`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `7`; crypto_alt avg `-0.1234` n `223`; crypto_major avg `-0.1592` n `7`; equity avg `0.0362` n `42`; fx avg `-0.026` n `4`; index avg `-0.0059` n `9`; metal avg `-0.0075` n `7`; unknown avg `-0.0389` n `311`
- 1h: commodity avg `-0.0134` n `7`; crypto_alt avg `-0.3067` n `223`; crypto_major avg `-0.1845` n `7`; equity avg `-0.1162` n `42`; fx avg `-0.0316` n `4`; index avg `-0.0198` n `9`; metal avg `-0.0093` n `7`; unknown avg `0.0196` n `311`
- 4h: commodity avg `-0.0443` n `7`; crypto_alt avg `-0.6343` n `223`; crypto_major avg `-0.3188` n `7`; equity avg `0.0184` n `42`; fx avg `-0.0665` n `4`; index avg `-0.0433` n `9`; metal avg `-0.0264` n `7`; unknown avg `-0.0243` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6555`, n `40`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6324`, n `40`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.6002`, n `36`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5794`, n `36`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5531`, n `36`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5458`, n `40`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5338`, n `36`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.5269`, n `36`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5106`, n `40`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5063`, n `40`, strong_sample_signal
