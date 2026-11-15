# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T11:37:27.312224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6424` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4753` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.1262` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.0981` n `239`; crypto_major avg `0.2765` n `8`; equity avg `0.0062` n `162`; fx avg `0.0041` n `6`; index avg `0.0011` n `27`; metal avg `0.0123` n `20`; unknown avg `-0.1341` n `1263`
- 1h: commodity avg `-0.0047` n `13`; crypto_alt avg `0.0158` n `239`; crypto_major avg `0.3685` n `8`; equity avg `0.0748` n `162`; fx avg `-0.008` n `6`; index avg `0.0051` n `27`; metal avg `0.0194` n `20`; unknown avg `0.4835` n `1257`
- 4h: commodity avg `-0.048` n `13`; crypto_alt avg `1.4088` n `239`; crypto_major avg `2.5944` n `8`; equity avg `0.4682` n `162`; fx avg `-0.0219` n `6`; index avg `0.0518` n `27`; metal avg `0.1191` n `20`; unknown avg `0.8937` n `1245`
- 24h: commodity avg `0.0337` n `13`; crypto_alt avg `-3.67` n `239`; crypto_major avg `-2.6429` n `8`; equity avg `-0.6395` n `162`; fx avg `0.0222` n `6`; index avg `-0.0493` n `27`; metal avg `-0.3202` n `20`; unknown avg `-0.276` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
