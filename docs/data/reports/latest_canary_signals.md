# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T11:52:23.638715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.049` n `230`; crypto_major avg `0.0216` n `8`; equity avg `-0.0262` n `113`; fx avg `-0.02` n `6`; index avg `0.0003` n `25`; metal avg `0.0348` n `20`; unknown avg `-0.0075` n `785`
- 1h: commodity avg `-0.1928` n `12`; crypto_alt avg `0.047` n `230`; crypto_major avg `0.1685` n `8`; equity avg `0.1765` n `113`; fx avg `-0.0422` n `6`; index avg `0.0186` n `25`; metal avg `0.0385` n `20`; unknown avg `-0.0914` n `785`
- 4h: commodity avg `-0.4332` n `12`; crypto_alt avg `0.2566` n `230`; crypto_major avg `0.5643` n `8`; equity avg `0.3327` n `113`; fx avg `-0.0724` n `6`; index avg `0.0808` n `25`; metal avg `0.3007` n `20`; unknown avg `-0.0613` n `785`
- 24h: commodity avg `0.48` n `12`; crypto_alt avg `-1.2837` n `230`; crypto_major avg `-0.4765` n `8`; equity avg `-0.695` n `113`; fx avg `-0.0492` n `6`; index avg `0.0996` n `25`; metal avg `0.4482` n `20`; unknown avg `0.0735` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
