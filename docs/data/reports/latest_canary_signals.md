# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T05:37:26.862797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.57` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.8535` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8085` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `-0.1251` n `239`; crypto_major avg `-0.2471` n `8`; equity avg `-0.0273` n `166`; fx avg `0.0001` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0152` n `20`; unknown avg `109.5124` n `1263`
- 1h: commodity avg `-0.0045` n `13`; crypto_alt avg `-0.574` n `239`; crypto_major avg `-0.8484` n `8`; equity avg `-0.2071` n `166`; fx avg `0.0074` n `6`; index avg `-0.0216` n `27`; metal avg `-0.0492` n `20`; unknown avg `168.5332` n `1263`
- 4h: commodity avg `-0.0851` n `13`; crypto_alt avg `-1.2071` n `239`; crypto_major avg `-1.9585` n `8`; equity avg `-0.6413` n `166`; fx avg `0.0005` n `6`; index avg `-0.105` n `27`; metal avg `-0.15` n `20`; unknown avg `23.153` n `1255`
- 24h: commodity avg `-0.0236` n `13`; crypto_alt avg `2.7219` n `239`; crypto_major avg `4.2439` n `8`; equity avg `1.3675` n `166`; fx avg `-0.0242` n `6`; index avg `0.1663` n `27`; metal avg `0.1439` n `20`; unknown avg `605.2314` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
