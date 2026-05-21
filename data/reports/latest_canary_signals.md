# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T13:52:22.601367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.22` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.7414` n `12`; crypto_alt avg `0.1778` n `228`; crypto_major avg `0.0657` n `8`; equity avg `0.0382` n `66`; fx avg `-0.0122` n `6`; index avg `0.2154` n `23`; metal avg `0.5009` n `18`; unknown avg `0.3783` n `386`
- 1h: commodity avg `-0.1931` n `12`; crypto_alt avg `0.1369` n `228`; crypto_major avg `0.1825` n `8`; equity avg `0.3809` n `66`; fx avg `-0.0476` n `6`; index avg `0.3004` n `23`; metal avg `0.2691` n `18`; unknown avg `0.3183` n `386`
- 4h: commodity avg `1.0419` n `12`; crypto_alt avg `-0.3695` n `228`; crypto_major avg `-0.3872` n `8`; equity avg `-0.2055` n `66`; fx avg `-0.071` n `6`; index avg `-0.1411` n `23`; metal avg `-0.3123` n `18`; unknown avg `1.5455` n `386`
- 24h: commodity avg `-1.0907` n `12`; crypto_alt avg `2.0618` n `228`; crypto_major avg `2.2862` n `8`; equity avg `1.6659` n `66`; fx avg `0.0052` n `6`; index avg `0.8985` n `23`; metal avg `0.4382` n `18`; unknown avg `6.6976` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
