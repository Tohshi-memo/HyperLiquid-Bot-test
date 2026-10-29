# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T13:52:33.928409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5008` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0334` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.8638` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0129` n `13`; crypto_alt avg `0.2475` n `238`; crypto_major avg `0.073` n `8`; equity avg `0.1915` n `156`; fx avg `0.0039` n `6`; index avg `0.0164` n `27`; metal avg `-0.0226` n `20`; unknown avg `0.7301` n `1236`
- 1h: commodity avg `-0.1978` n `13`; crypto_alt avg `0.1922` n `238`; crypto_major avg `0.2588` n `8`; equity avg `0.0642` n `156`; fx avg `-0.0489` n `6`; index avg `-0.07` n `27`; metal avg `-0.0622` n `20`; unknown avg `5.1115` n `1232`
- 4h: commodity avg `-0.5726` n `13`; crypto_alt avg `1.3199` n `238`; crypto_major avg `1.9282` n `8`; equity avg `0.0644` n `155`; fx avg `-0.0116` n `6`; index avg `-0.1722` n `27`; metal avg `-0.1052` n `20`; unknown avg `22.8046` n `1140`
- 24h: commodity avg `-0.8929` n `13`; crypto_alt avg `0.0576` n `238`; crypto_major avg `1.4186` n `8`; equity avg `-0.5799` n `155`; fx avg `-0.0561` n `6`; index avg `-0.1235` n `27`; metal avg `-0.593` n `20`; unknown avg `12.3945` n `980`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
