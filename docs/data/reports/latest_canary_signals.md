# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T10:00:31.411550+00:00`
- Correlation status: `ready`
- Asset price records: `350`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `7`; crypto_alt avg `0.0377` n `223`; crypto_major avg `0.0496` n `7`; equity avg `-0.1251` n `47`; fx avg `-0.0093` n `4`; index avg `0.0235` n `6`; metal avg `-0.0202` n `7`; unknown avg `1.1672` n `312`
- 1h: commodity avg `0.1173` n `7`; crypto_alt avg `0.0111` n `223`; crypto_major avg `-0.1871` n `7`; equity avg `-0.0838` n `47`; fx avg `0.0228` n `4`; index avg `0.0442` n `6`; metal avg `0.0663` n `7`; unknown avg `1.1611` n `312`
- 4h: commodity avg `-0.098` n `7`; crypto_alt avg `0.168` n `223`; crypto_major avg `-0.258` n `7`; equity avg `0.1051` n `47`; fx avg `0.0518` n `4`; index avg `0.1442` n `6`; metal avg `0.3402` n `7`; unknown avg `0.393` n `312`
- 24h: commodity avg `0.5475` n `7`; crypto_alt avg `0.5657` n `223`; crypto_major avg `0.1195` n `7`; equity avg `-0.0025` n `47`; fx avg `0.0204` n `4`; index avg `0.1754` n `6`; metal avg `0.1659` n `7`; unknown avg `0.1571` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2172`, n `346`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.21`, n `346`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1395`, n `346`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `346`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `346`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `346`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `346`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `346`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `342`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.094`, n `342`, weak_sample_signal
