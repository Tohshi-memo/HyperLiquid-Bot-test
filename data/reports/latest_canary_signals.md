# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T15:37:30.501138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.25` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `3.5841` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.1776` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-3.1625` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-2.9151` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.2622` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.2044` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.1525` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1558` n `12`; crypto_alt avg `-1.4084` n `228`; crypto_major avg `-0.9369` n `8`; equity avg `-0.0477` n `69`; fx avg `0.0005` n `6`; index avg `0.0852` n `23`; metal avg `0.0807` n `18`; unknown avg `-0.5106` n `422`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `-2.3633` n `228`; crypto_major avg `-1.9032` n `8`; equity avg `0.2493` n `69`; fx avg `-0.0156` n `6`; index avg `0.359` n `23`; metal avg `0.3012` n `18`; unknown avg `-0.9121` n `422`
- 4h: commodity avg `0.1039` n `12`; crypto_alt avg `-3.6325` n `228`; crypto_major avg `-3.0737` n `8`; equity avg `0.0888` n `69`; fx avg `-0.0102` n `6`; index avg `0.5104` n `23`; metal avg `-0.1586` n `18`; unknown avg `-0.5532` n `422`
- 24h: commodity avg `-0.8692` n `12`; crypto_alt avg `-3.3999` n `228`; crypto_major avg `-3.6574` n `8`; equity avg `0.2752` n `69`; fx avg `0.1803` n `6`; index avg `0.7301` n `23`; metal avg `0.842` n `18`; unknown avg `-0.9653` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
