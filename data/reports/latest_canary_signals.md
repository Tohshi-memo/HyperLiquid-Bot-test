# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T23:37:19.798539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.3351` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.609` n `228`; crypto_major avg `-0.2341` n `8`; equity avg `0.105` n `69`; fx avg `-0.0107` n `6`; index avg `0.0567` n `23`; metal avg `-0.0094` n `18`; unknown avg `-0.2727` n `422`
- 1h: commodity avg `0.5621` n `12`; crypto_alt avg `-1.8533` n `228`; crypto_major avg `-1.0061` n `8`; equity avg `-0.5819` n `69`; fx avg `-0.0253` n `6`; index avg `-0.1624` n `23`; metal avg `-0.4782` n `18`; unknown avg `-0.4137` n `422`
- 4h: commodity avg `0.6341` n `12`; crypto_alt avg `-0.9385` n `228`; crypto_major avg `-1.2547` n `8`; equity avg `0.0811` n `69`; fx avg `-0.0635` n `6`; index avg `0.0804` n `23`; metal avg `-0.4074` n `18`; unknown avg `-0.014` n `422`
- 24h: commodity avg `0.6252` n `12`; crypto_alt avg `-5.9648` n `228`; crypto_major avg `-6.7544` n `8`; equity avg `0.7092` n `69`; fx avg `0.0377` n `6`; index avg `0.6144` n `23`; metal avg `-0.1491` n `18`; unknown avg `-0.8142` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
