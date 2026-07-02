# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T12:52:29.014036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3367` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7465` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0243` n `12`; crypto_alt avg `-0.0212` n `229`; crypto_major avg `0.0611` n `8`; equity avg `-0.161` n `88`; fx avg `0.0482` n `6`; index avg `-0.0497` n `25`; metal avg `-0.0913` n `20`; unknown avg `-0.0673` n `763`
- 1h: commodity avg `0.1037` n `12`; crypto_alt avg `0.3256` n `229`; crypto_major avg `0.3303` n `8`; equity avg `0.9364` n `88`; fx avg `0.043` n `6`; index avg `0.1958` n `25`; metal avg `0.6018` n `20`; unknown avg `0.1571` n `763`
- 4h: commodity avg `-0.0638` n `12`; crypto_alt avg `1.2362` n `228`; crypto_major avg `2.2729` n `8`; equity avg `1.2634` n `88`; fx avg `0.0021` n `6`; index avg `0.2098` n `25`; metal avg `0.5264` n `20`; unknown avg `0.0566` n `763`
- 24h: commodity avg `-0.3888` n `12`; crypto_alt avg `3.7954` n `228`; crypto_major avg `5.0314` n `8`; equity avg `0.129` n `88`; fx avg `-0.0506` n `6`; index avg `-0.2367` n `25`; metal avg `1.2622` n `20`; unknown avg `2.0376` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
