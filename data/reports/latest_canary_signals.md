# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T00:52:31.259118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3297` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2594` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.2234` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0324` n `12`; crypto_alt avg `0.0583` n `230`; crypto_major avg `-0.0003` n `8`; equity avg `-0.015` n `121`; fx avg `-0.001` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.163` n `793`
- 1h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.7087` n `230`; crypto_major avg `-0.2093` n `8`; equity avg `0.0029` n `121`; fx avg `0.0009` n `6`; index avg `0.0034` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0294` n `793`
- 4h: commodity avg `-0.0562` n `12`; crypto_alt avg `2.3614` n `230`; crypto_major avg `2.2735` n `8`; equity avg `0.0501` n `121`; fx avg `0.0043` n `6`; index avg `0.0319` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0407` n `793`
- 24h: commodity avg `0.065` n `12`; crypto_alt avg `8.8999` n `230`; crypto_major avg `6.5661` n `8`; equity avg `0.4492` n `121`; fx avg `-0.0239` n `6`; index avg `0.0415` n `25`; metal avg `0.4755` n `20`; unknown avg `1.2819` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
