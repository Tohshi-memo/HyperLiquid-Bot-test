# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T05:07:38.273694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.2485` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.158` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.0844` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.7865` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `-0.692` n `239`; crypto_major avg `-0.6649` n `8`; equity avg `-0.1185` n `166`; fx avg `-0.0046` n `6`; index avg `-0.007` n `27`; metal avg `-0.0295` n `20`; unknown avg `159.7802` n `1252`
- 1h: commodity avg `0.0301` n `13`; crypto_alt avg `0.8302` n `239`; crypto_major avg `0.6163` n `8`; equity avg `0.175` n `166`; fx avg `-0.0008` n `6`; index avg `0.0451` n `27`; metal avg `0.0889` n `20`; unknown avg `285.124` n `1248`
- 4h: commodity avg `-0.0261` n `13`; crypto_alt avg `-3.4706` n `239`; crypto_major avg `-4.2746` n `8`; equity avg `-1.4881` n `166`; fx avg `-0.0313` n `6`; index avg `-0.1166` n `27`; metal avg `-0.1902` n `20`; unknown avg `1.2818` n `1242`
- 24h: commodity avg `0.2811` n `13`; crypto_alt avg `-6.4884` n `239`; crypto_major avg `-8.4487` n `8`; equity avg `-5.5979` n `166`; fx avg `-0.0449` n `6`; index avg `-0.5813` n `27`; metal avg `-0.037` n `20`; unknown avg `12.4617` n `1109`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
