# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T07:52:26.378344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5788` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1822` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `-1.1718` n `231`; crypto_major avg `-1.082` n `8`; equity avg `-0.1199` n `122`; fx avg `-0.0062` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.2099` n `794`
- 1h: commodity avg `0.0509` n `12`; crypto_alt avg `-0.8791` n `231`; crypto_major avg `-0.8252` n `8`; equity avg `-0.1646` n `122`; fx avg `0.0209` n `6`; index avg `-0.0355` n `25`; metal avg `-0.0591` n `20`; unknown avg `-0.1861` n `794`
- 4h: commodity avg `-0.1846` n `12`; crypto_alt avg `-1.178` n `231`; crypto_major avg `-1.0712` n `8`; equity avg `0.5076` n `122`; fx avg `0.0301` n `6`; index avg `0.111` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.2629` n `778`
- 24h: commodity avg `-0.2186` n `12`; crypto_alt avg `0.5049` n `231`; crypto_major avg `1.3834` n `8`; equity avg `0.1715` n `122`; fx avg `0.0362` n `6`; index avg `0.0355` n `25`; metal avg `-0.1519` n `20`; unknown avg `0.3505` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
