# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T20:52:30.336260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.1198` n `234`; crypto_major avg `-0.0695` n `8`; equity avg `0.017` n `141`; fx avg `-0.0127` n `6`; index avg `0.004` n `26`; metal avg `0.0275` n `20`; unknown avg `6.5766` n `945`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `-0.5072` n `234`; crypto_major avg `-0.4534` n `8`; equity avg `0.0804` n `141`; fx avg `-0.0155` n `6`; index avg `0.0382` n `26`; metal avg `0.0472` n `20`; unknown avg `7.1629` n `861`
- 4h: commodity avg `0.1888` n `12`; crypto_alt avg `-0.8124` n `234`; crypto_major avg `0.0733` n `8`; equity avg `-0.0962` n `141`; fx avg `-0.0109` n `6`; index avg `0.0317` n `26`; metal avg `0.1032` n `20`; unknown avg `6.8449` n `853`
- 24h: commodity avg `0.6127` n `12`; crypto_alt avg `-3.9483` n `234`; crypto_major avg `-3.6018` n `8`; equity avg `-1.6008` n `140`; fx avg `0.0084` n `6`; index avg `-0.3411` n `26`; metal avg `-0.8059` n `20`; unknown avg `572.9333` n `836`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
