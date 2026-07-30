# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T05:07:26.347846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0456` n `12`; crypto_alt avg `-0.167` n `230`; crypto_major avg `-0.1764` n `8`; equity avg `-0.1994` n `102`; fx avg `-0.0203` n `6`; index avg `-0.062` n `25`; metal avg `-0.0689` n `20`; unknown avg `-0.1682` n `779`
- 1h: commodity avg `0.0778` n `12`; crypto_alt avg `-0.3216` n `230`; crypto_major avg `-0.288` n `8`; equity avg `-0.492` n `102`; fx avg `-0.0421` n `6`; index avg `-0.0865` n `25`; metal avg `-0.1392` n `20`; unknown avg `-0.2151` n `779`
- 4h: commodity avg `0.0925` n `12`; crypto_alt avg `-0.0455` n `230`; crypto_major avg `-0.2599` n `8`; equity avg `-1.444` n `102`; fx avg `-0.0594` n `6`; index avg `-0.2072` n `25`; metal avg `-0.4296` n `20`; unknown avg `0.0309` n `779`
- 24h: commodity avg `0.6667` n `12`; crypto_alt avg `-0.4285` n `230`; crypto_major avg `-0.451` n `8`; equity avg `-2.5638` n `102`; fx avg `0.0665` n `6`; index avg `-0.108` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.5198` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
