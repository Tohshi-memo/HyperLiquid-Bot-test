# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T16:22:32.212102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0455` n `230`; crypto_major avg `-0.0077` n `8`; equity avg `-0.0227` n `92`; fx avg `0.0152` n `6`; index avg `0.0092` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.0585` n `765`
- 1h: commodity avg `0.0371` n `12`; crypto_alt avg `-0.0446` n `230`; crypto_major avg `0.0772` n `8`; equity avg `-0.0852` n `92`; fx avg `-0.0085` n `6`; index avg `0.0245` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.0604` n `765`
- 4h: commodity avg `0.0442` n `12`; crypto_alt avg `0.0655` n `230`; crypto_major avg `0.4641` n `8`; equity avg `-0.0433` n `92`; fx avg `-0.0064` n `6`; index avg `0.0515` n `25`; metal avg `-0.0201` n `20`; unknown avg `-0.0722` n `765`
- 24h: commodity avg `0.5103` n `12`; crypto_alt avg `-0.8502` n `230`; crypto_major avg `-0.2593` n `8`; equity avg `-0.0919` n `92`; fx avg `0.0375` n `6`; index avg `-0.0807` n `25`; metal avg `-0.1004` n `20`; unknown avg `0.2098` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
