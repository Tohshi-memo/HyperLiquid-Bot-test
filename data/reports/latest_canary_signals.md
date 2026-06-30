# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T14:52:35.287083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2859` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0436` n `12`; crypto_alt avg `-0.2251` n `228`; crypto_major avg `-0.4166` n `8`; equity avg `-0.4088` n `88`; fx avg `0.023` n `6`; index avg `-0.024` n `23`; metal avg `-0.1092` n `20`; unknown avg `-0.1811` n `765`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `0.2407` n `228`; crypto_major avg `-0.1362` n `8`; equity avg `0.0902` n `88`; fx avg `0.0571` n `6`; index avg `0.0397` n `23`; metal avg `0.2361` n `20`; unknown avg `-0.2716` n `765`
- 4h: commodity avg `0.1597` n `12`; crypto_alt avg `-0.7077` n `228`; crypto_major avg `-1.1082` n `8`; equity avg `0.0955` n `88`; fx avg `0.0407` n `6`; index avg `0.1777` n `23`; metal avg `0.0661` n `20`; unknown avg `-0.0207` n `765`
- 24h: commodity avg `0.317` n `12`; crypto_alt avg `-1.0528` n `228`; crypto_major avg `-0.5954` n `8`; equity avg `2.3426` n `88`; fx avg `0.13` n `6`; index avg `0.4714` n `23`; metal avg `0.4591` n `20`; unknown avg `7.8938` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
