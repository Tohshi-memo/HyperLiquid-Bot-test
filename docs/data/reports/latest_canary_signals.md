# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T20:07:33.623073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6738` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6207` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `0.0642` n `233`; crypto_major avg `0.2474` n `8`; equity avg `-0.1852` n `136`; fx avg `0.0117` n `6`; index avg `-0.0382` n `27`; metal avg `-0.0119` n `20`; unknown avg `6.4371` n `894`
- 1h: commodity avg `0.1203` n `12`; crypto_alt avg `-0.0891` n `233`; crypto_major avg `0.1407` n `8`; equity avg `-0.4697` n `136`; fx avg `0.0278` n `6`; index avg `-0.0951` n `27`; metal avg `-0.1603` n `20`; unknown avg `14.8252` n `894`
- 4h: commodity avg `-0.1431` n `12`; crypto_alt avg `1.1193` n `233`; crypto_major avg `1.5495` n `8`; equity avg `-0.1243` n `136`; fx avg `0.029` n `6`; index avg `-0.0372` n `27`; metal avg `-0.0712` n `20`; unknown avg `2.7188` n `866`
- 24h: commodity avg `0.1716` n `12`; crypto_alt avg `0.4588` n `233`; crypto_major avg `2.5542` n `8`; equity avg `-0.7708` n `136`; fx avg `0.0687` n `6`; index avg `-0.2283` n `27`; metal avg `-0.4808` n `20`; unknown avg `2.1509` n `684`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
