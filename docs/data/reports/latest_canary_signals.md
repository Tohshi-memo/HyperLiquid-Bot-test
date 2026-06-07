# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T13:07:25.310022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `79.09` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_commodity_crypto_divergence: score `-2.455` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9758` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8467` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7431` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0824` n `12`; crypto_alt avg `0.03` n `228`; crypto_major avg `-0.1004` n `8`; equity avg `-0.0674` n `74`; fx avg `0.0001` n `6`; index avg `0.0022` n `23`; metal avg `-0.0382` n `18`; unknown avg `0.0275` n `516`
- 1h: commodity avg `0.213` n `12`; crypto_alt avg `-1.0619` n `228`; crypto_major avg `-1.068` n `8`; equity avg `-0.2557` n `74`; fx avg `0.008` n `6`; index avg `-0.0806` n `23`; metal avg `-0.1819` n `18`; unknown avg `-0.0183` n `516`
- 4h: commodity avg `0.2336` n `12`; crypto_alt avg `-2.0691` n `228`; crypto_major avg `-2.2214` n `8`; equity avg `-0.4783` n `74`; fx avg `-0.0027` n `6`; index avg `-0.2456` n `23`; metal avg `-0.3747` n `18`; unknown avg `-3.3377` n `516`
- 24h: commodity avg `0.227` n `12`; crypto_alt avg `1.2413` n `228`; crypto_major avg `1.2364` n `8`; equity avg `1.2491` n `74`; fx avg `0.0307` n `6`; index avg `0.2529` n `23`; metal avg `0.3158` n `18`; unknown avg `-0.2622` n `405`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
