# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T20:37:29.678602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.041` n `234`; crypto_major avg `-0.0798` n `8`; equity avg `0.0033` n `140`; fx avg `0.0009` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0144` n `20`; unknown avg `5.3058` n `913`
- 1h: commodity avg `0.0497` n `12`; crypto_alt avg `0.3273` n `234`; crypto_major avg `0.314` n `8`; equity avg `0.0724` n `140`; fx avg `-0.0062` n `6`; index avg `-0.021` n `26`; metal avg `-0.027` n `20`; unknown avg `16.3293` n `885`
- 4h: commodity avg `-0.0799` n `12`; crypto_alt avg `0.4708` n `234`; crypto_major avg `0.4365` n `8`; equity avg `0.0853` n `140`; fx avg `0.0076` n `6`; index avg `-0.0135` n `26`; metal avg `-0.1927` n `20`; unknown avg `5.0769` n `885`
- 24h: commodity avg `-0.1254` n `12`; crypto_alt avg `4.2331` n `234`; crypto_major avg `1.9106` n `8`; equity avg `2.5145` n `138`; fx avg `-0.0246` n `6`; index avg `0.4522` n `26`; metal avg `0.5551` n `20`; unknown avg `6.0151` n `771`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
