# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T09:37:26.815638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.0743` n `238`; crypto_major avg `-0.076` n `8`; equity avg `-0.2015` n `154`; fx avg `0.012` n `6`; index avg `-0.0237` n `27`; metal avg `-0.0229` n `20`; unknown avg `2.6812` n `1222`
- 1h: commodity avg `-0.0218` n `13`; crypto_alt avg `-0.0189` n `238`; crypto_major avg `-0.212` n `8`; equity avg `-0.1897` n `154`; fx avg `0.009` n `6`; index avg `-0.0201` n `27`; metal avg `0.0118` n `20`; unknown avg `2.7183` n `1202`
- 4h: commodity avg `-0.0442` n `13`; crypto_alt avg `0.2888` n `238`; crypto_major avg `0.5352` n `8`; equity avg `-0.0314` n `154`; fx avg `0.0204` n `6`; index avg `-0.0039` n `27`; metal avg `0.0655` n `20`; unknown avg `42.3105` n `1168`
- 24h: commodity avg `-0.2375` n `13`; crypto_alt avg `2.4155` n `238`; crypto_major avg `2.7101` n `8`; equity avg `3.4316` n `154`; fx avg `0.1198` n `6`; index avg `0.4617` n `27`; metal avg `0.3966` n `20`; unknown avg `7.9728` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
