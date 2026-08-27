# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T05:52:25.535323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `0.4752` n `231`; crypto_major avg `0.5521` n `8`; equity avg `0.0512` n `127`; fx avg `0.0085` n `6`; index avg `0.0084` n `26`; metal avg `-0.1079` n `20`; unknown avg `0.4442` n `791`
- 1h: commodity avg `-0.0661` n `12`; crypto_alt avg `0.2052` n `231`; crypto_major avg `0.6246` n `8`; equity avg `-0.0743` n `127`; fx avg `0.0068` n `6`; index avg `-0.0314` n `26`; metal avg `-0.1626` n `20`; unknown avg `-0.1792` n `791`
- 4h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.6227` n `231`; crypto_major avg `-0.1782` n `8`; equity avg `-0.0837` n `127`; fx avg `0.0333` n `6`; index avg `-0.0648` n `26`; metal avg `-0.2678` n `20`; unknown avg `-0.2217` n `791`
- 24h: commodity avg `0.2819` n `12`; crypto_alt avg `0.0008` n `231`; crypto_major avg `0.5609` n `8`; equity avg `1.0823` n `127`; fx avg `-0.0811` n `6`; index avg `0.1873` n `26`; metal avg `-0.4221` n `20`; unknown avg `0.3457` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
