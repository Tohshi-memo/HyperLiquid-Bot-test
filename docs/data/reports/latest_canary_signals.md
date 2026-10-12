# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T12:07:26.900847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `0.1692` n `235`; crypto_major avg `-0.0301` n `8`; equity avg `-0.0779` n `151`; fx avg `0.0097` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0092` n `20`; unknown avg `-0.0537` n `1126`
- 1h: commodity avg `0.0878` n `13`; crypto_alt avg `-0.1657` n `235`; crypto_major avg `-0.2494` n `8`; equity avg `-0.0752` n `151`; fx avg `0.0132` n `6`; index avg `0.0085` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.0909` n `1125`
- 4h: commodity avg `0.4581` n `13`; crypto_alt avg `-1.0335` n `235`; crypto_major avg `-0.8744` n `8`; equity avg `-0.7059` n `151`; fx avg `-0.0018` n `6`; index avg `-0.1201` n `26`; metal avg `-0.0249` n `20`; unknown avg `0.2648` n `1019`
- 24h: commodity avg `0.121` n `13`; crypto_alt avg `1.1925` n `235`; crypto_major avg `0.6472` n `8`; equity avg `-1.4433` n `151`; fx avg `-0.1374` n `6`; index avg `-0.1713` n `26`; metal avg `0.0178` n `20`; unknown avg `0.7161` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2459`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
