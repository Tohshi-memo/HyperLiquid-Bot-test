# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T18:52:26.585317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-2.7418` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.6139` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.5059` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-2.1928` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.04` n `12`; crypto_alt avg `-1.1344` n `233`; crypto_major avg `-1.448` n `8`; equity avg `-0.2295` n `137`; fx avg `-0.0008` n `6`; index avg `-0.0186` n `27`; metal avg `0.0614` n `20`; unknown avg `3.8316` n `918`
- 1h: commodity avg `-0.1124` n `12`; crypto_alt avg `-2.4744` n `233`; crypto_major avg `-2.6183` n `8`; equity avg `-0.4255` n `137`; fx avg `0.0` n `6`; index avg `-0.0044` n `27`; metal avg `0.1235` n `20`; unknown avg `8.8012` n `915`
- 4h: commodity avg `0.0932` n `12`; crypto_alt avg `-0.7398` n `233`; crypto_major avg `-0.9347` n `8`; equity avg `-0.2198` n `137`; fx avg `0.0116` n `6`; index avg `0.0249` n `27`; metal avg `0.3125` n `20`; unknown avg `-0.0838` n `901`
- 24h: commodity avg `0.6915` n `12`; crypto_alt avg `-4.8328` n `233`; crypto_major avg `-5.3988` n `8`; equity avg `-1.8295` n `137`; fx avg `0.2382` n `6`; index avg `-0.1921` n `27`; metal avg `0.1386` n `20`; unknown avg `0.5101` n `831`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
