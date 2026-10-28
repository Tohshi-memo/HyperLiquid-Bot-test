# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T04:07:29.142008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0316` n `13`; crypto_alt avg `-0.3012` n `238`; crypto_major avg `-0.2534` n `8`; equity avg `-0.0929` n `154`; fx avg `-0.0003` n `6`; index avg `-0.0225` n `27`; metal avg `-0.0434` n `20`; unknown avg `0.1774` n `1224`
- 1h: commodity avg `0.023` n `13`; crypto_alt avg `-0.0961` n `238`; crypto_major avg `0.0258` n `8`; equity avg `0.2994` n `154`; fx avg `0.0219` n `6`; index avg `0.0042` n `27`; metal avg `-0.0382` n `20`; unknown avg `0.5722` n `1222`
- 4h: commodity avg `0.1056` n `13`; crypto_alt avg `0.3577` n `238`; crypto_major avg `0.3714` n `8`; equity avg `1.2167` n `154`; fx avg `0.1446` n `6`; index avg `0.1789` n `27`; metal avg `-0.1845` n `20`; unknown avg `0.5543` n `1214`
- 24h: commodity avg `0.0138` n `13`; crypto_alt avg `2.2632` n `237`; crypto_major avg `2.0162` n `8`; equity avg `3.2514` n `154`; fx avg `0.0989` n `6`; index avg `0.4699` n `27`; metal avg `0.1194` n `20`; unknown avg `6.0875` n `1014`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
