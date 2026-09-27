# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T13:52:31.455554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0572` n `234`; crypto_major avg `-0.0584` n `8`; equity avg `-0.0084` n `141`; fx avg `0.0069` n `6`; index avg `-0.0061` n `26`; metal avg `0.0021` n `20`; unknown avg `1.1481` n `962`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.7049` n `234`; crypto_major avg `-0.6153` n `8`; equity avg `-0.0432` n `141`; fx avg `0.0072` n `6`; index avg `-0.0123` n `26`; metal avg `0.0044` n `20`; unknown avg `1.5541` n `960`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `-0.818` n `234`; crypto_major avg `-0.4795` n `8`; equity avg `-0.0454` n `141`; fx avg `0.0005` n `6`; index avg `-0.0216` n `26`; metal avg `-0.0138` n `20`; unknown avg `2.8382` n `954`
- 24h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.1861` n `234`; crypto_major avg `0.5875` n `8`; equity avg `0.3256` n `141`; fx avg `-0.0246` n `6`; index avg `0.0201` n `26`; metal avg `-0.0114` n `20`; unknown avg `72.4834` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
