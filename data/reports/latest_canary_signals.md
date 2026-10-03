# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T01:07:28.067638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `-0.0382` n `235`; crypto_major avg `-0.0781` n `8`; equity avg `-0.0107` n `143`; fx avg `0.013` n `6`; index avg `0.001` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.0539` n `982`
- 1h: commodity avg `-0.0922` n `13`; crypto_alt avg `0.3279` n `235`; crypto_major avg `0.2404` n `8`; equity avg `-0.0398` n `143`; fx avg `0.0225` n `6`; index avg `0.0057` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.5888` n `982`
- 4h: commodity avg `0.0791` n `13`; crypto_alt avg `1.8508` n `235`; crypto_major avg `1.0217` n `8`; equity avg `0.0425` n `143`; fx avg `0.0136` n `6`; index avg `0.0029` n `26`; metal avg `0.0043` n `20`; unknown avg `0.822` n `960`
- 24h: commodity avg `0.1929` n `13`; crypto_alt avg `0.0594` n `235`; crypto_major avg `-0.0753` n `8`; equity avg `0.7106` n `142`; fx avg `-0.1641` n `6`; index avg `0.2879` n `26`; metal avg `-0.0592` n `20`; unknown avg `-0.4561` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
