# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T03:52:28.321081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5396` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.2396` n `228`; crypto_major avg `0.1008` n `8`; equity avg `0.0993` n `88`; fx avg `-0.0021` n `6`; index avg `0.0382` n `23`; metal avg `-0.0236` n `20`; unknown avg `-0.1205` n `763`
- 1h: commodity avg `0.0413` n `12`; crypto_alt avg `0.667` n `228`; crypto_major avg `0.5117` n `8`; equity avg `0.3116` n `88`; fx avg `0.0127` n `6`; index avg `0.0749` n `23`; metal avg `0.02` n `20`; unknown avg `-0.0913` n `763`
- 4h: commodity avg `-0.0561` n `12`; crypto_alt avg `1.2275` n `228`; crypto_major avg `1.0961` n `8`; equity avg `-0.4435` n `88`; fx avg `0.0766` n `6`; index avg `-0.1485` n `23`; metal avg `-0.3474` n `20`; unknown avg `0.9372` n `763`
- 24h: commodity avg `0.1211` n `12`; crypto_alt avg `-0.3358` n `228`; crypto_major avg `0.0716` n `8`; equity avg `0.7476` n `88`; fx avg `0.1709` n `6`; index avg `0.0631` n `23`; metal avg `-0.0314` n `20`; unknown avg `6.7336` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
