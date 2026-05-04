# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T18:00:30.433317+00:00`
- Correlation status: `ready`
- Asset price records: `286`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.0148` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9121` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0187` n `7`; crypto_alt avg `-0.0528` n `223`; crypto_major avg `-0.1095` n `7`; equity avg `-0.0393` n `42`; fx avg `0.0005` n `4`; index avg `-0.0016` n `9`; metal avg `-0.0193` n `7`; unknown avg `0.0627` n `314`
- 1h: commodity avg `-0.3572` n `7`; crypto_alt avg `0.6596` n `223`; crypto_major avg `0.5352` n `7`; equity avg `0.0731` n `42`; fx avg `0.0177` n `4`; index avg `0.0328` n `9`; metal avg `0.2614` n `7`; unknown avg `0.1269` n `314`
- 4h: commodity avg `0.8991` n `7`; crypto_alt avg `1.1011` n `223`; crypto_major avg `1.1418` n `7`; equity avg `-0.7703` n `42`; fx avg `-0.0135` n `4`; index avg `-0.2456` n `9`; metal avg `-0.873` n `7`; unknown avg `-0.2879` n `314`
- 24h: commodity avg `1.7598` n `7`; crypto_alt avg `2.2012` n `223`; crypto_major avg `1.5014` n `7`; equity avg `-0.0974` n `42`; fx avg `-0.081` n `4`; index avg `0.4977` n `9`; metal avg `-2.2335` n `7`; unknown avg `-0.7268` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2376`, n `282`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2316`, n `282`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1614`, n `278`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1603`, n `278`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `282`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `282`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `282`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1401`, n `278`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1392`, n `278`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.131`, n `278`, weak_sample_signal
