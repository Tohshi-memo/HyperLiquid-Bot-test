# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T18:15:30.148403+00:00`
- Correlation status: `ready`
- Asset price records: `287`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.5547` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.536` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0199` n `7`; crypto_alt avg `-0.0688` n `223`; crypto_major avg `-0.1149` n `7`; equity avg `-0.1242` n `42`; fx avg `-0.0008` n `4`; index avg `0.0153` n `9`; metal avg `-0.0637` n `7`; unknown avg `0.0172` n `314`
- 1h: commodity avg `-0.1931` n `7`; crypto_alt avg `0.2653` n `223`; crypto_major avg `0.0131` n `7`; equity avg `0.0625` n `42`; fx avg `0.0049` n `4`; index avg `-0.153` n `9`; metal avg `-0.0822` n `7`; unknown avg `0.0545` n `314`
- 4h: commodity avg `0.9222` n `7`; crypto_alt avg `0.6783` n `223`; crypto_major avg `0.479` n `7`; equity avg `-1.0757` n `42`; fx avg `-0.0214` n `4`; index avg `-0.4101` n `9`; metal avg `-1.057` n `7`; unknown avg `-0.2655` n `314`
- 24h: commodity avg `1.7191` n `7`; crypto_alt avg `2.1705` n `223`; crypto_major avg `1.4916` n `7`; equity avg `-0.1886` n `42`; fx avg `-0.0664` n `4`; index avg `0.5325` n `9`; metal avg `-2.3728` n `7`; unknown avg `-0.7543` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2376`, n `283`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2317`, n `283`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1593`, n `279`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1584`, n `279`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1537`, n `283`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `283`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `283`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1314`, n `279`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1309`, n `279`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1296`, n `279`, weak_sample_signal
