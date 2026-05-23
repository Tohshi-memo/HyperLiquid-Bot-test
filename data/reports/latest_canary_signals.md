# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T20:52:17.632685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6756` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.2956` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0591` n `12`; crypto_alt avg `1.0068` n `228`; crypto_major avg `0.6976` n `8`; equity avg `0.2161` n `67`; fx avg `0.0192` n `6`; index avg `-0.0114` n `23`; metal avg `0.1745` n `18`; unknown avg `-0.2085` n `396`
- 1h: commodity avg `-0.9451` n `12`; crypto_alt avg `1.4233` n `228`; crypto_major avg `1.3505` n `8`; equity avg `0.3971` n `67`; fx avg `0.0613` n `6`; index avg `0.1738` n `23`; metal avg `0.4418` n `18`; unknown avg `0.2214` n `396`
- 4h: commodity avg `-1.6098` n `12`; crypto_alt avg `2.4395` n `228`; crypto_major avg `2.0658` n `8`; equity avg `0.959` n `67`; fx avg `0.0248` n `6`; index avg `0.5859` n `23`; metal avg `0.5924` n `18`; unknown avg `2.2177` n `396`
- 24h: commodity avg `-1.6476` n `12`; crypto_alt avg `2.0813` n `228`; crypto_major avg `1.905` n `8`; equity avg `1.0431` n `67`; fx avg `0.0197` n `6`; index avg `0.5891` n `23`; metal avg `0.7063` n `18`; unknown avg `-0.3021` n `376`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
