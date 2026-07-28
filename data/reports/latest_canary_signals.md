# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T01:22:27.292604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.376` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1767` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1253` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `0.1926` n `230`; crypto_major avg `0.1807` n `8`; equity avg `-0.0206` n `102`; fx avg `0.0037` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0659` n `20`; unknown avg `0.1061` n `773`
- 1h: commodity avg `0.0182` n `12`; crypto_alt avg `-0.6674` n `230`; crypto_major avg `-0.5788` n `8`; equity avg `-0.5296` n `102`; fx avg `-0.0031` n `6`; index avg `-0.0691` n `25`; metal avg `-0.1928` n `20`; unknown avg `0.4241` n `773`
- 4h: commodity avg `-0.0899` n `12`; crypto_alt avg `-2.7112` n `230`; crypto_major avg `-2.4659` n `8`; equity avg `-1.6264` n `102`; fx avg `0.0728` n `6`; index avg `-0.2892` n `25`; metal avg `-0.3406` n `20`; unknown avg `2.4577` n `773`
- 24h: commodity avg `-0.8428` n `12`; crypto_alt avg `-4.1581` n `230`; crypto_major avg `-3.4028` n `8`; equity avg `-2.5199` n `102`; fx avg `-0.0357` n `6`; index avg `-0.5626` n `25`; metal avg `-0.3694` n `20`; unknown avg `1163.3858` n `756`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3516`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3171`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
