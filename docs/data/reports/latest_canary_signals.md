# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T17:07:50.674237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6178` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.1001` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9478` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0533` n `12`; crypto_alt avg `-0.4925` n `233`; crypto_major avg `-0.4826` n `8`; equity avg `-0.1747` n `137`; fx avg `0.0083` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0321` n `20`; unknown avg `-0.2442` n `915`
- 1h: commodity avg `0.1354` n `12`; crypto_alt avg `-0.0638` n `233`; crypto_major avg `-0.2934` n `8`; equity avg `-0.0073` n `137`; fx avg `-0.0087` n `6`; index avg `0.0202` n `27`; metal avg `0.0504` n `20`; unknown avg `-0.3394` n `901`
- 4h: commodity avg `0.5028` n `12`; crypto_alt avg `-1.4107` n `233`; crypto_major avg `-2.115` n `8`; equity avg `-0.9303` n `137`; fx avg `0.0606` n `6`; index avg `-0.1672` n `27`; metal avg `-0.0149` n `20`; unknown avg `1.1318` n `873`
- 24h: commodity avg `0.5769` n `12`; crypto_alt avg `-2.6918` n `233`; crypto_major avg `-2.9343` n `8`; equity avg `-1.3419` n `137`; fx avg `0.2284` n `6`; index avg `-0.1718` n `27`; metal avg `-0.0636` n `20`; unknown avg `0.4782` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
