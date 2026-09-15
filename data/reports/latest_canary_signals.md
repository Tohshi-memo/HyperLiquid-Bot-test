# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T22:22:33.354670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5684` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5487` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.4904` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.2156` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0399` n `12`; crypto_alt avg `-0.1927` n `234`; crypto_major avg `-0.2091` n `8`; equity avg `-0.017` n `137`; fx avg `0.0086` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0025` n `20`; unknown avg `-0.0882` n `919`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.7899` n `234`; crypto_major avg `-0.4974` n `8`; equity avg `-0.0722` n `137`; fx avg `0.0135` n `6`; index avg `-0.0032` n `27`; metal avg `0.0193` n `20`; unknown avg `6.2229` n `877`
- 4h: commodity avg `0.0319` n `12`; crypto_alt avg `-2.3373` n `234`; crypto_major avg `-2.5365` n `8`; equity avg `-0.3209` n `137`; fx avg `0.005` n `6`; index avg `0.0122` n `27`; metal avg `-0.0461` n `20`; unknown avg `1.0879` n `853`
- 24h: commodity avg `0.4837` n `12`; crypto_alt avg `-4.6776` n `234`; crypto_major avg `-5.0787` n `8`; equity avg `-1.3343` n `137`; fx avg `0.2303` n `6`; index avg `-0.0665` n `27`; metal avg `0.1741` n `20`; unknown avg `2.347` n `810`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
