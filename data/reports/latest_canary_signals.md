# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T23:52:26.758063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.1406` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0308` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.0164` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.1109` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.05` n `13`; crypto_alt avg `0.078` n `235`; crypto_major avg `-0.0292` n `8`; equity avg `-0.0861` n `151`; fx avg `0.002` n `6`; index avg `-0.0274` n `26`; metal avg `-0.0234` n `20`; unknown avg `1.7947` n `1135`
- 1h: commodity avg `-0.1005` n `13`; crypto_alt avg `-1.1458` n `235`; crypto_major avg `-1.178` n `8`; equity avg `-0.4847` n `151`; fx avg `0.0045` n `6`; index avg `-0.0671` n `26`; metal avg `-0.0167` n `20`; unknown avg `1.1182` n `1133`
- 4h: commodity avg `-0.0934` n `13`; crypto_alt avg `-2.5365` n `235`; crypto_major avg `-2.1098` n `8`; equity avg `-0.643` n `151`; fx avg `0.0011` n `6`; index avg `-0.079` n `26`; metal avg `0.0308` n `20`; unknown avg `2.8969` n `1060`
- 24h: commodity avg `0.6032` n `13`; crypto_alt avg `-5.4963` n `235`; crypto_major avg `-3.8203` n `8`; equity avg `-4.1001` n `151`; fx avg `-0.1643` n `6`; index avg `-0.432` n `26`; metal avg `-0.1411` n `20`; unknown avg `0.4404` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2046`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1783`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0822`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `666`, weak_sample_signal
