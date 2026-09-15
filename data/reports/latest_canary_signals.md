# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T00:37:33.486164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.3564` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.2644` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2225` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.017` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.1276` n `233`; crypto_major avg `0.0933` n `8`; equity avg `0.1165` n `136`; fx avg `0.0008` n `6`; index avg `0.0098` n `27`; metal avg `0.0107` n `20`; unknown avg `0.1543` n `902`
- 1h: commodity avg `0.0793` n `12`; crypto_alt avg `0.1259` n `233`; crypto_major avg `-0.0164` n `8`; equity avg `0.2257` n `136`; fx avg `0.0316` n `6`; index avg `0.0798` n `27`; metal avg `-0.0823` n `20`; unknown avg `0.2438` n `900`
- 4h: commodity avg `0.1377` n `12`; crypto_alt avg `-1.41` n `233`; crypto_major avg `-2.1267` n `8`; equity avg `0.2297` n `136`; fx avg `0.0271` n `6`; index avg `0.0958` n `27`; metal avg `-0.1097` n `20`; unknown avg `2.8134` n `878`
- 24h: commodity avg `-0.0918` n `12`; crypto_alt avg `1.1677` n `233`; crypto_major avg `2.0255` n `8`; equity avg `0.3068` n `136`; fx avg `0.0424` n `6`; index avg `0.0587` n `27`; metal avg `-0.4433` n `20`; unknown avg `6.4282` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
