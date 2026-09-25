# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T23:37:29.547131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.1876` n `234`; crypto_major avg `-0.096` n `8`; equity avg `-0.0181` n `141`; fx avg `0.0014` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.0563` n `960`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.1229` n `234`; crypto_major avg `-0.0679` n `8`; equity avg `-0.0093` n `141`; fx avg `0.0019` n `6`; index avg `0.0037` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0228` n `958`
- 4h: commodity avg `0.0892` n `12`; crypto_alt avg `0.7076` n `234`; crypto_major avg `0.2322` n `8`; equity avg `0.0611` n `141`; fx avg `-0.011` n `6`; index avg `0.0332` n `26`; metal avg `-0.0372` n `20`; unknown avg `0.2211` n `852`
- 24h: commodity avg `-0.3849` n `12`; crypto_alt avg `2.9157` n `234`; crypto_major avg `1.112` n `8`; equity avg `0.127` n `141`; fx avg `-0.2685` n `6`; index avg `0.2511` n `26`; metal avg `0.1579` n `20`; unknown avg `1122.0658` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
