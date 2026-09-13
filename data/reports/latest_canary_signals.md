# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T23:22:26.958159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0006` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.0153` n `233`; crypto_major avg `-0.0548` n `8`; equity avg `-0.0162` n `136`; fx avg `-0.0197` n `6`; index avg `0.0008` n `27`; metal avg `-0.0351` n `20`; unknown avg `0.91` n `840`
- 1h: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.131` n `233`; crypto_major avg `-0.0498` n `8`; equity avg `-0.0659` n `136`; fx avg `-0.0237` n `6`; index avg `0.0366` n `27`; metal avg `0.0501` n `20`; unknown avg `0.5858` n `838`
- 4h: commodity avg `0.3205` n `12`; crypto_alt avg `-1.674` n `233`; crypto_major avg `-1.0388` n `8`; equity avg `-0.3814` n `136`; fx avg `0.0124` n `6`; index avg `-0.0382` n `27`; metal avg `-0.0691` n `20`; unknown avg `14.2945` n `802`
- 24h: commodity avg `0.6366` n `12`; crypto_alt avg `-1.6331` n `233`; crypto_major avg `-1.7294` n `8`; equity avg `-1.4956` n `136`; fx avg `0.0299` n `6`; index avg `-0.2812` n `26`; metal avg `-0.129` n `20`; unknown avg `2.6092` n `716`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
