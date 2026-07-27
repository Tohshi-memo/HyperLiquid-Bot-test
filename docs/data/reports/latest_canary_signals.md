# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T14:37:32.900692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.029` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-1.728` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5861` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5387` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3941` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2336` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `-1.0144` n `230`; crypto_major avg `-0.9651` n `8`; equity avg `-1.0554` n `102`; fx avg `-0.005` n `6`; index avg `-0.172` n `25`; metal avg `-0.0914` n `20`; unknown avg `-0.2681` n `774`
- 1h: commodity avg `-0.0737` n `12`; crypto_alt avg `-1.7925` n `230`; crypto_major avg `-1.884` n `8`; equity avg `-2.9938` n `102`; fx avg `-0.0316` n `6`; index avg `-0.4899` n `25`; metal avg `-0.156` n `20`; unknown avg `-0.0345` n `774`
- 4h: commodity avg `0.2016` n `12`; crypto_alt avg `-1.901` n `230`; crypto_major avg `-1.8274` n `8`; equity avg `-3.4135` n `102`; fx avg `-0.0347` n `6`; index avg `-0.5938` n `25`; metal avg `-0.2887` n `20`; unknown avg `-0.1269` n `773`
- 24h: commodity avg `-0.5132` n `12`; crypto_alt avg `-1.1649` n `230`; crypto_major avg `-0.4681` n `8`; equity avg `-2.254` n `102`; fx avg `0.0568` n `6`; index avg `-0.4452` n `25`; metal avg `0.0806` n `20`; unknown avg `-0.3049` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
