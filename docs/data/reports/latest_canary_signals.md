# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T17:58:54.978642+00:00`
- Correlation status: `ready`
- Asset price records: `285`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9844` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5225` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0006` n `7`; crypto_alt avg `0.2413` n `223`; crypto_major avg `0.1937` n `7`; equity avg `0.0417` n `42`; fx avg `0.0018` n `4`; index avg `-0.1811` n `9`; metal avg `-0.0181` n `7`; unknown avg `-0.015` n `314`
- 1h: commodity avg `-0.2856` n `7`; crypto_alt avg `0.6128` n `223`; crypto_major avg `0.437` n `7`; equity avg `0.0584` n `42`; fx avg `0.0142` n `4`; index avg `0.0176` n `9`; metal avg `0.2598` n `7`; unknown avg `0.0159` n `314`
- 4h: commodity avg `0.7917` n `7`; crypto_alt avg `1.1093` n `223`; crypto_major avg `1.2469` n `7`; equity avg `-0.2756` n `42`; fx avg `-0.0114` n `4`; index avg `-0.2805` n `9`; metal avg `-0.7375` n `7`; unknown avg `-0.4254` n `314`
- 24h: commodity avg `1.9259` n `7`; crypto_alt avg `2.2848` n `223`; crypto_major avg `1.555` n `7`; equity avg `-0.0745` n `42`; fx avg `-0.0817` n `4`; index avg `0.4847` n `9`; metal avg `-2.2601` n `7`; unknown avg `-0.7833` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2387`, n `281`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2328`, n `281`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1637`, n `277`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1626`, n `277`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1531`, n `281`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `281`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1439`, n `277`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `281`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1434`, n `277`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1395`, n `277`, weak_sample_signal
