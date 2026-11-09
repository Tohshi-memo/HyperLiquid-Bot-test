# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T00:37:29.986527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.4338` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1658` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0747` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0577` n `13`; crypto_alt avg `0.1045` n `239`; crypto_major avg `0.1445` n `8`; equity avg `0.046` n `158`; fx avg `0.0248` n `6`; index avg `-0.0147` n `27`; metal avg `0.1125` n `20`; unknown avg `-0.0451` n `1262`
- 1h: commodity avg `-0.0332` n `13`; crypto_alt avg `0.0286` n `239`; crypto_major avg `-0.2803` n `8`; equity avg `-0.3344` n `158`; fx avg `-0.0391` n `6`; index avg `-0.0349` n `27`; metal avg `0.1928` n `20`; unknown avg `1.848` n `1248`
- 4h: commodity avg `-0.0125` n `13`; crypto_alt avg `-1.405` n `239`; crypto_major avg `-2.1783` n `8`; equity avg `-0.8972` n `158`; fx avg `-0.075` n `6`; index avg `-0.1036` n `27`; metal avg `0.2555` n `20`; unknown avg `0.9469` n `1194`
- 24h: commodity avg `0.0489` n `13`; crypto_alt avg `-2.7682` n `239`; crypto_major avg `-2.4606` n `8`; equity avg `-0.831` n `158`; fx avg `-0.0266` n `6`; index avg `-0.1487` n `27`; metal avg `0.2257` n `20`; unknown avg `-0.022` n `1000`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
