# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T13:41:25.530884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.3274` n `8`; equity avg `-0.3874` n `113`; fx avg `0.008` n `6`; index avg `-0.068` n `25`; metal avg `-0.079` n `20`; unknown avg `0.0659` n `786`
- 1h: commodity avg `-0.1841` n `12`; crypto_alt avg `-0.249` n `230`; crypto_major avg `-0.4924` n `8`; equity avg `-0.0759` n `113`; fx avg `-0.0116` n `6`; index avg `0.0434` n `25`; metal avg `-0.1727` n `20`; unknown avg `0.0335` n `786`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `-0.3041` n `8`; equity avg `0.5895` n `113`; fx avg `0.0164` n `6`; index avg `0.0772` n `25`; metal avg `-0.0957` n `20`; unknown avg `-0.1074` n `786`
- 24h: commodity avg `0.1899` n `12`; crypto_alt avg `-0.7573` n `230`; crypto_major avg `0.5993` n `8`; equity avg `2.7508` n `113`; fx avg `0.0337` n `6`; index avg `0.2969` n `25`; metal avg `0.2053` n `20`; unknown avg `-0.1674` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.242`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
