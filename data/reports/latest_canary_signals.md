# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T03:37:28.350972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1642` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0499` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8948` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `0.1101` n `238`; crypto_major avg `0.0474` n `8`; equity avg `0.1706` n `155`; fx avg `-0.004` n `6`; index avg `0.0564` n `27`; metal avg `0.0215` n `20`; unknown avg `1.3047` n `1236`
- 1h: commodity avg `-0.0526` n `13`; crypto_alt avg `-0.0005` n `238`; crypto_major avg `0.1063` n `8`; equity avg `0.2056` n `155`; fx avg `-0.0027` n `6`; index avg `0.056` n `27`; metal avg `-0.0553` n `20`; unknown avg `2.9675` n `1222`
- 4h: commodity avg `-0.0008` n `13`; crypto_alt avg `-2.7874` n `238`; crypto_major avg `-2.165` n `8`; equity avg `-0.9709` n `155`; fx avg `-0.1029` n `6`; index avg `-0.1151` n `27`; metal avg `-0.2702` n `20`; unknown avg `5.1612` n `1198`
- 24h: commodity avg `-0.0606` n `13`; crypto_alt avg `-2.8496` n `238`; crypto_major avg `-2.1603` n `8`; equity avg `-1.531` n `154`; fx avg `-0.0025` n `6`; index avg `-0.1705` n `27`; metal avg `-0.2726` n `20`; unknown avg `28.6698` n `982`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
