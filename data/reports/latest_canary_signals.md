# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T21:46:09.228674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.5437` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.4801` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3571` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.943` n `238`; crypto_major avg `-0.7287` n `8`; equity avg `-0.0306` n `156`; fx avg `0.0042` n `6`; index avg `0.0226` n `27`; metal avg `0.0071` n `20`; unknown avg `2.0686` n `1258`
- 1h: commodity avg `-0.0417` n `13`; crypto_alt avg `0.2592` n `238`; crypto_major avg `0.4409` n `8`; equity avg `-0.4276` n `156`; fx avg `-0.0115` n `6`; index avg `-0.0216` n `27`; metal avg `0.0039` n `20`; unknown avg `155.8939` n `1246`
- 4h: commodity avg `0.0033` n `13`; crypto_alt avg `-4.2546` n `238`; crypto_major avg `-2.4768` n `8`; equity avg `-2.2088` n `156`; fx avg `0.0079` n `6`; index avg `-0.1197` n `27`; metal avg `0.0669` n `20`; unknown avg `24.6771` n `1162`
- 24h: commodity avg `-0.2579` n `13`; crypto_alt avg `-5.585` n `238`; crypto_major avg `-1.7983` n `8`; equity avg `-3.1063` n `155`; fx avg `0.051` n `6`; index avg `-0.2311` n `27`; metal avg `-0.586` n `20`; unknown avg `33.0392` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
