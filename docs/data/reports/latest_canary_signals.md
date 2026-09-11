# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T13:52:33.718519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.156` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.9222` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.9138` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `1.8101` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0869` n `12`; crypto_alt avg `1.6348` n `233`; crypto_major avg `2.189` n `8`; equity avg `0.246` n `136`; fx avg `0.0257` n `6`; index avg `-0.0299` n `26`; metal avg `-0.0127` n `20`; unknown avg `3.1966` n `782`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.9834` n `233`; crypto_major avg `1.4974` n `8`; equity avg `-0.3127` n `136`; fx avg `-0.0131` n `6`; index avg `-0.0463` n `26`; metal avg `0.0665` n `20`; unknown avg `0.699` n `780`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `2.3152` n `233`; crypto_major avg `3.1932` n `8`; equity avg `0.271` n `136`; fx avg `-0.0726` n `6`; index avg `0.0679` n `26`; metal avg `0.2794` n `20`; unknown avg `0.4115` n `774`
- 24h: commodity avg `-0.0111` n `12`; crypto_alt avg `1.5901` n `233`; crypto_major avg `2.9405` n `8`; equity avg `0.435` n `136`; fx avg `-0.1424` n `6`; index avg `0.2487` n `26`; metal avg `0.0888` n `20`; unknown avg `2.1667` n `685`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
