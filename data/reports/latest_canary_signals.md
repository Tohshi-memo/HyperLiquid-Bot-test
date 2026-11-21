# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T10:07:39.943033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2462` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.0378` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3587` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.214` n `239`; crypto_major avg `-0.0663` n `8`; equity avg `0.0076` n `166`; fx avg `0.0327` n `6`; index avg `-0.0027` n `27`; metal avg `0.0032` n `20`; unknown avg `161.8021` n `1252`
- 1h: commodity avg `-0.017` n `13`; crypto_alt avg `0.2289` n `239`; crypto_major avg `0.1104` n `8`; equity avg `0.12` n `166`; fx avg `0.0139` n `6`; index avg `0.0248` n `27`; metal avg `0.0109` n `20`; unknown avg `306.5492` n `1256`
- 4h: commodity avg `-0.0522` n `13`; crypto_alt avg `2.1521` n `239`; crypto_major avg `3.194` n `8`; equity avg `0.8353` n `166`; fx avg `-0.0447` n `6`; index avg `0.0818` n `27`; metal avg `0.1562` n `20`; unknown avg `164.0177` n `1230`
- 24h: commodity avg `0.8495` n `13`; crypto_alt avg `-5.5938` n `239`; crypto_major avg `-6.4826` n `8`; equity avg `-4.3525` n `166`; fx avg `-0.0652` n `6`; index avg `-0.4821` n `27`; metal avg `-0.3707` n `20`; unknown avg `347.8192` n `1149`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
