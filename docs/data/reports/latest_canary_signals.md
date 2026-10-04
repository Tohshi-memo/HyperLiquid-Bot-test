# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T20:07:25.139666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `-0.0407` n `235`; crypto_major avg `-0.0875` n `8`; equity avg `0.0043` n `144`; fx avg `0.0067` n `6`; index avg `0.0024` n `26`; metal avg `-0.0176` n `20`; unknown avg `1.8137` n `1064`
- 1h: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.0086` n `235`; crypto_major avg `-0.067` n `8`; equity avg `0.0246` n `144`; fx avg `-0.0001` n `6`; index avg `0.0032` n `26`; metal avg `-0.0043` n `20`; unknown avg `3.0405` n `1064`
- 4h: commodity avg `0.0188` n `13`; crypto_alt avg `0.3895` n `235`; crypto_major avg `0.2583` n `8`; equity avg `0.0467` n `144`; fx avg `-0.0091` n `6`; index avg `0.0055` n `26`; metal avg `0.0109` n `20`; unknown avg `1.6674` n `1064`
- 24h: commodity avg `0.0251` n `13`; crypto_alt avg `0.9098` n `235`; crypto_major avg `0.778` n `8`; equity avg `0.1707` n `144`; fx avg `0.0193` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.9514` n `1020`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
