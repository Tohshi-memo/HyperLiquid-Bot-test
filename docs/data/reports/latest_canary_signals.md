# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T07:07:24.531322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `0.0049` n `230`; crypto_major avg `0.0609` n `8`; equity avg `-0.1385` n `121`; fx avg `0.0162` n `6`; index avg `-0.014` n `25`; metal avg `-0.0306` n `20`; unknown avg `-0.0046` n `792`
- 1h: commodity avg `0.0747` n `12`; crypto_alt avg `0.5552` n `230`; crypto_major avg `0.7889` n `8`; equity avg `0.1046` n `121`; fx avg `-0.0135` n `6`; index avg `0.0125` n `25`; metal avg `-0.0549` n `20`; unknown avg `0.3383` n `792`
- 4h: commodity avg `0.101` n `12`; crypto_alt avg `0.7489` n `230`; crypto_major avg `1.2933` n `8`; equity avg `0.1555` n `121`; fx avg `-0.0003` n `6`; index avg `0.0232` n `25`; metal avg `-0.0841` n `20`; unknown avg `0.2561` n `776`
- 24h: commodity avg `-0.0233` n `12`; crypto_alt avg `5.8369` n `230`; crypto_major avg `10.6352` n `8`; equity avg `1.0908` n `120`; fx avg `0.0733` n `6`; index avg `0.2388` n `25`; metal avg `1.0103` n `20`; unknown avg `1.9535` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
