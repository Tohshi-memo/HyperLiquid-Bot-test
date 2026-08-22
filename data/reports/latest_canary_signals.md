# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T04:52:29.166685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `5.5403` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `5.5008` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `5.4297` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.3419` n `230`; crypto_major avg `0.045` n `8`; equity avg `-0.0077` n `121`; fx avg `-0.0046` n `6`; index avg `0.0108` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.302` n `794`
- 1h: commodity avg `0.0441` n `12`; crypto_alt avg `1.2167` n `230`; crypto_major avg `1.4267` n `8`; equity avg `-0.0477` n `121`; fx avg `0.002` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0269` n `20`; unknown avg `0.4728` n `794`
- 4h: commodity avg `0.0648` n `12`; crypto_alt avg `4.8105` n `230`; crypto_major avg `5.4945` n `8`; equity avg `-0.0063` n `121`; fx avg `0.0359` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0458` n `20`; unknown avg `0.9542` n `793`
- 24h: commodity avg `0.1598` n `12`; crypto_alt avg `13.0165` n `230`; crypto_major avg `11.444` n `8`; equity avg `0.2828` n `121`; fx avg `0.0684` n `6`; index avg `-0.0168` n `25`; metal avg `0.1535` n `20`; unknown avg `2.253` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
