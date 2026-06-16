# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T18:37:49.252219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0889` n `12`; crypto_alt avg `-0.0475` n `228`; crypto_major avg `-0.1268` n `8`; equity avg `-0.1284` n `77`; fx avg `-0.0057` n `6`; index avg `-0.0296` n `23`; metal avg `0.025` n `18`; unknown avg `0.0266` n `687`
- 1h: commodity avg `0.1864` n `12`; crypto_alt avg `0.5526` n `228`; crypto_major avg `0.3549` n `8`; equity avg `0.1981` n `77`; fx avg `-0.0044` n `6`; index avg `0.0888` n `23`; metal avg `0.1318` n `18`; unknown avg `0.3032` n `687`
- 4h: commodity avg `-0.1206` n `12`; crypto_alt avg `1.2922` n `228`; crypto_major avg `0.5727` n `8`; equity avg `0.0032` n `77`; fx avg `0.0781` n `6`; index avg `-0.2583` n `23`; metal avg `0.3951` n `18`; unknown avg `0.8802` n `687`
- 24h: commodity avg `-0.9871` n `12`; crypto_alt avg `-0.9599` n `228`; crypto_major avg `-0.9294` n `8`; equity avg `-0.9434` n `77`; fx avg `-0.0102` n `6`; index avg `-0.6607` n `23`; metal avg `0.5929` n `18`; unknown avg `0.8135` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0424`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0416`, n `668`, weak_sample_signal
