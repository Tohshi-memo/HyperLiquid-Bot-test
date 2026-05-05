# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T05:45:27.190258+00:00`
- Correlation status: `ready`
- Asset price records: `333`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0153` n `7`; crypto_alt avg `-0.0792` n `223`; crypto_major avg `0.0427` n `7`; equity avg `-0.033` n `47`; fx avg `0.0043` n `4`; index avg `0.0117` n `6`; metal avg `0.139` n `7`; unknown avg `-0.2899` n `312`
- 1h: commodity avg `0.086` n `7`; crypto_alt avg `0.0916` n `223`; crypto_major avg `0.3282` n `7`; equity avg `0.5724` n `47`; fx avg `-0.0112` n `4`; index avg `0.0422` n `6`; metal avg `0.3448` n `7`; unknown avg `0.927` n `312`
- 4h: commodity avg `-0.1452` n `7`; crypto_alt avg `0.3085` n `223`; crypto_major avg `0.7885` n `7`; equity avg `0.7262` n `47`; fx avg `-0.0112` n `4`; index avg `0.2632` n `6`; metal avg `0.4817` n `7`; unknown avg `1.4055` n `312`
- 24h: commodity avg `1.2519` n `7`; crypto_alt avg `0.453` n `223`; crypto_major avg `-0.1402` n `7`; equity avg `-0.2759` n `47`; fx avg `-0.0268` n `4`; index avg `-0.1755` n `6`; metal avg `-1.3487` n `7`; unknown avg `0.0256` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2247`, n `329`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2181`, n `329`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.142`, n `329`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1401`, n `329`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `329`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `329`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `329`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1148`, n `325`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1116`, n `325`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `329`, weak_sample_signal
