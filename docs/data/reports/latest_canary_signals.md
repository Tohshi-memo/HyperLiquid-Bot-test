# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T04:07:31.746840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6383` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.5542` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4845` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.2627` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.1516` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.2105` n `239`; crypto_major avg `-0.0379` n `8`; equity avg `0.0268` n `162`; fx avg `-0.0016` n `6`; index avg `0.0` n `27`; metal avg `-0.012` n `20`; unknown avg `-0.0902` n `1250`
- 1h: commodity avg `-0.0522` n `13`; crypto_alt avg `-0.5973` n `239`; crypto_major avg `-1.1624` n `8`; equity avg `-0.1227` n `162`; fx avg `-0.007` n `6`; index avg `-0.0108` n `27`; metal avg `-0.0464` n `20`; unknown avg `0.1284` n `1248`
- 4h: commodity avg `0.004` n `13`; crypto_alt avg `-1.925` n `239`; crypto_major avg `-2.6343` n `8`; equity avg `-0.3716` n `162`; fx avg `-0.0194` n `6`; index avg `-0.1498` n `27`; metal avg `-0.0801` n `20`; unknown avg `7.017` n `1248`
- 24h: commodity avg `-0.1721` n `13`; crypto_alt avg `-0.7636` n `239`; crypto_major avg `-2.4817` n `8`; equity avg `-2.7944` n `162`; fx avg `-0.099` n `6`; index avg `-0.2275` n `27`; metal avg `-0.6711` n `20`; unknown avg `63.0262` n `1032`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
