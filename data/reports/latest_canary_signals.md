# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T07:07:23.881465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9031` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0272` n `13`; crypto_alt avg `-0.0249` n `238`; crypto_major avg `-0.0349` n `8`; equity avg `-0.0952` n `156`; fx avg `0.0266` n `6`; index avg `0.0119` n `27`; metal avg `-0.0258` n `20`; unknown avg `128.6669` n `1252`
- 1h: commodity avg `-0.005` n `13`; crypto_alt avg `0.4221` n `238`; crypto_major avg `0.1603` n `8`; equity avg `0.0816` n `156`; fx avg `-0.0021` n `6`; index avg `0.0592` n `27`; metal avg `-0.0574` n `20`; unknown avg `132.4685` n `1250`
- 4h: commodity avg `-0.0745` n `13`; crypto_alt avg `2.4276` n `238`; crypto_major avg `1.7714` n `8`; equity avg `0.3761` n `156`; fx avg `-0.0164` n `6`; index avg `0.127` n `27`; metal avg `-0.1317` n `20`; unknown avg `3.2149` n `1214`
- 24h: commodity avg `-0.1076` n `13`; crypto_alt avg `-2.8201` n `238`; crypto_major avg `0.3892` n `8`; equity avg `-2.7916` n `155`; fx avg `0.1319` n `6`; index avg `-0.3434` n `27`; metal avg `-0.7568` n `20`; unknown avg `30.0126` n `978`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
