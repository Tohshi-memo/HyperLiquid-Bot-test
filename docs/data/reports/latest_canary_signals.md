# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T14:22:37.779028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0734` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6006` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5557` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.416` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.2243` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.1454` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `-2.7815` n `234`; crypto_major avg `-2.3713` n `8`; equity avg `-0.7138` n `140`; fx avg `0.0058` n `6`; index avg `-0.0923` n `26`; metal avg `-0.0794` n `20`; unknown avg `4.0397` n `944`
- 1h: commodity avg `0.0591` n `12`; crypto_alt avg `-3.1233` n `234`; crypto_major avg `-2.3569` n `8`; equity avg `-1.2904` n `140`; fx avg `0.0126` n `6`; index avg `-0.2115` n `26`; metal avg `-0.1326` n `20`; unknown avg `515.9293` n `904`
- 4h: commodity avg `0.2006` n `12`; crypto_alt avg `-3.8806` n `234`; crypto_major avg `-2.8728` n `8`; equity avg `-1.5138` n `140`; fx avg `0.0199` n `6`; index avg `-0.2722` n `26`; metal avg `-0.3171` n `20`; unknown avg `518.301` n `898`
- 24h: commodity avg `0.3797` n `12`; crypto_alt avg `-1.3407` n `234`; crypto_major avg `-3.0023` n `8`; equity avg `-1.5836` n `140`; fx avg `0.0441` n `6`; index avg `-0.3383` n `26`; metal avg `-0.5738` n `20`; unknown avg `22.1165` n `830`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
